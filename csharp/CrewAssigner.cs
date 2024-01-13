using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Application
{

    public enum jobType
    {
        TURRET,
        RADAR,
        SHIELD,
        HELM,
        

    }
    public static class CrewAssigner
    {

        public static Dictionary<Crewmate, jobType> AssignCrew(List<jobType> JobsNeeded, Crewmate[] crewmates)
        {
            Dictionary<Crewmate, jobType> assignedCrewmates = new Dictionary<Crewmate, jobType>();
            
            Dictionary<jobType, List<Crewmate>> candidatesPerJob = new();
            foreach(jobType job in JobsNeeded.Distinct())
            {
                candidatesPerJob.Add(job, crewmates.Where(x => CanAccessJob(x, job) == true).ToList());
            }


            foreach(jobType job in JobsNeeded.OrderBy(x=> candidatesPerJob[x].Count))
            {
               var crewmate = candidatesPerJob[job].Where(x => !assignedCrewmates.Keys.Any(y => x == y)).FirstOrDefault();
                if(crewmate != null)
                {
                    assignedCrewmates.Add(crewmate, job);
                }
            }
            
            foreach(var unassignedCrew in crewmates.Where(x=> assignedCrewmates.Keys.Any(y=> x == y)))
            {
                assignedCrewmates.Add(unassignedCrew, assignJobByPriority(unassignedCrew));
            }


            return assignedCrewmates;
        }

        private static jobType assignJobByPriority(Crewmate unassignedCrew)
        {
            if (unassignedCrew.DistanceFromStations.Turrets.Length > 0)
                return jobType.TURRET;
            else if(unassignedCrew.DistanceFromStations.Radars.Length > 0)            
                return jobType.RADAR;
            else if (unassignedCrew.DistanceFromStations.Shields.Length > 0)
                return jobType.SHIELD;
            else
                return jobType.HELM;
        }

        private static bool CanAccessJob(Crewmate x, jobType job)
        {
            switch (job)
            {
                case jobType.TURRET:
                    return x.DistanceFromStations.Turrets.Length > 0;
                case jobType.HELM:
                    return x.DistanceFromStations.Helms.Length > 0;
                case jobType.SHIELD:
                    return x.DistanceFromStations.Shields.Length > 0;
                case jobType.RADAR:
                    return x.DistanceFromStations.Radars.Length > 0;
                default:
                    return false;
            }
        }
    }

}
