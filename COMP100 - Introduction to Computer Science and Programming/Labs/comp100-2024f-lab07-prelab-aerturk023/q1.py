paths = [
    "/home/user/docs/file1.txt",
    "/home/user/docs/file2.txt",
    "/home/user/videos/ibiza_trip.mp4",
    "/home/user/videos/christmas_party.mp4",
    "/home/user/videos/movies/isle_of_dogs.mp4",
    "/home/user/videos/movies/la_haine.mp4",
    "/home/user/downloads",
    "/home/system/system32",
    "/home/system/config.ini",
    "/dev/input/mouse",
    "/dev/input/gamepad/ps5_controller_conf.ini",
] # Do not change paths list

def reconstruct_dir(paths):
    """Recursively inserts components into the directory tree. Returns the directory tree."""

    directory = []
    
    for file in paths:
        file = file.strip("/").split("/")
        subdir = directory
        for i in range(len(file)):
            if file[i] in subdir:
                subdir = subdir[subdir.index(file[i])+1]
            else:
                if "." in file[i]:
                    subdir.append(file[i])
                else:
                    subdir.append(file[i])
                    subdir.append([])
                    subdir = subdir[subdir.index(file[i])+1]
    
    return directory
