package spaceMission;

public class MissionControl {

	private Mission[] missions;
	private int currentMissionIndex = 0;
	
	public MissionControl(int numberOfMissions) {
		this.missions = new Mission[numberOfMissions];
	}
	
	public void addMission(Mission mission) {
		if (!(currentMissionIndex < missions.length)) {
			System.out.println("Cannot add more missions. Maximum limit reached.");
		} else {
			missions[currentMissionIndex] = mission;
			currentMissionIndex++;
		}
	}
	
	public void startExpedition() {
		for (Mission m: missions) {
			System.out.println("\n--------------------- New Mission -------------------\n");
			m.getPlanet().displayPlanetInfo();
			System.out.println("\nMission Details:");
			m.displayMissionDetails();
			m.getAlien().interact("What were you doing on this planet?", m.getAlien());
			System.out.println("Mission Expedition Completed.");
		}
	}
	
}
