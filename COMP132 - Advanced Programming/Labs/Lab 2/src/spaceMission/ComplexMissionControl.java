package spaceMission;

public class ComplexMissionControl {

	private ComplexMission[] missions;
	private int currentMissionIndex = 0;
	
	public ComplexMissionControl(int numberOfMissions) {
		missions = new ComplexMission[numberOfMissions];
	}
	
	public void addComplexMission(ComplexMission complexMission) {
		if (currentMissionIndex < missions.length) {
			missions[currentMissionIndex] = complexMission;
			currentMissionIndex++;
		} else {
			System.out.println("Cannot add more missions. Maximum limit reached.");
		}
	}
	
	public void startExpedition() {
		for (ComplexMission cm:missions) {
			System.out.println("--------------------- New Mission -------------------\nInvestigating the Mission:\n\n");
			cm.getPlanet().displayPlanetInfo();
			cm.displayComplexMissionDetails();
			System.out.printf("\nExpedition:\nThe Astronaut for this mission is: %s%n%n", cm.getAstronaut().getName());
			Alien.interact("What were you doing on this planet site?", cm.getAliens());
			System.out.println("Mission Investigation Completed.");
		}
	}
}
