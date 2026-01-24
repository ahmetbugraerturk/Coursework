import unittest
from q1 import reconstruct_dir

class TestReconstructDir(unittest.TestCase):
    def test_basic_structure(self):
        paths = [
            "/home/user/docs/file1.txt",
            "/home/user/docs/file2.txt",
            "/home/user/videos/ibiza_trip.mp4",
        ]
        expected = [
            "home", [
                "user", [
                    "docs", [
                        "file1.txt",
                        "file2.txt"
                    ],
                    "videos", [
                        "ibiza_trip.mp4"
                    ]
                ]
            ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_nested_directories(self):
        paths = [
            "/home/user/videos/movies/isle_of_dogs.mp4",
            "/home/user/videos/movies/la_haine.mp4",
        ]
        expected = [
            "home", [
                "user", [
                    "videos", [
                        "movies", [
                            "isle_of_dogs.mp4",
                            "la_haine.mp4"
                        ]
                    ]
                ]
            ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_empty_directory(self):
        paths = [
            "/home/user/downloads",
            "/home/user/docs/",
        ]
        expected = [
            "home", [
                "user", [
                    "downloads", [],
                    "docs", []
                ]
            ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_system_paths(self):
        paths = [
            "/home/system/system32",
            "/home/system/config.ini",
            "/dev/input/mouse",
        ]
        expected = [
            "home", [
                "system", [
                    "system32", [],
                    "config.ini"
                ]
            ],
            "dev", [
                "input", [
                    "mouse", []
                ]
            ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_mixed_files_and_directories(self):
        paths = [
            "/home/user/docs/file1.txt",
            "/home/user/docs/file2.txt",
            "/dev/input/gamepad/ps5_controller_conf.ini",
        ]
        expected = [
            "home", [
                "user", [
                    "docs", [
                        "file1.txt",
                        "file2.txt"
                    ]
                ]
            ],
            "dev", [
                "input", [
                    "gamepad", [
                        "ps5_controller_conf.ini"
                    ]
                ]
            ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_no_paths(self):
        paths = []
        expected = []
        self.assertEqual(reconstruct_dir(paths), expected)

    def test_root_files_only(self):
        paths = [
            "/file1.txt",
            "/file2.txt",
        ]
        expected = [
            "file1.txt",
            "file2.txt"
        ]
        self.assertEqual(reconstruct_dir(paths), expected)
    def test_actual_paths(self):
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
        ]
        expected = [
            'home', [
                'user', [
                    'docs', ['file1.txt', 'file2.txt'], 
                    'videos', [
                        'ibiza_trip.mp4', 'christmas_party.mp4', 
                        'movies', ['isle_of_dogs.mp4', 'la_haine.mp4']
                            ], 
                    'downloads', []
                        ], 
                'system', ['system32', [], 'config.ini']
                    ], 
            'dev', [
                'input', ['mouse', [], 'gamepad', ['ps5_controller_conf.ini']]
                ]
        ]
        self.assertEqual(reconstruct_dir(paths), expected)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReconstructDir)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
