import unittest

import auto_semver


class TestAutoSemver(unittest.TestCase):
    def setUp(self):
        self.semver_list_minor = [
            {
                "semver": "0.1.0",
                "major": "0",
                "minor": "1",
                "patch": "0",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "0.6.3",
                "major": "0",
                "minor": "6",
                "patch": "3",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "0.3.65",
                "major": "0",
                "minor": "3",
                "patch": "65",
                "prerelease": None,
                "buildmetadata": None,
            },
        ]

        self.semver_list_major = [
            {
                "semver": "2.1.0",
                "major": "2",
                "minor": "1",
                "patch": "0",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "1.6.3",
                "major": "1",
                "minor": "6",
                "patch": "3",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "0.3.65",
                "major": "0",
                "minor": "3",
                "patch": "65",
                "prerelease": None,
                "buildmetadata": None,
            },
        ]

        self.semver_list_patch = [
            {
                "semver": "1.6.23",
                "major": "2",
                "minor": "1",
                "patch": "0",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "1.6.3",
                "major": "1",
                "minor": "6",
                "patch": "3",
                "prerelease": None,
                "buildmetadata": None,
            },
            {
                "semver": "0.3.65",
                "major": "0",
                "minor": "3",
                "patch": "65",
                "prerelease": None,
                "buildmetadata": None,
            },
        ]

    def test_get_highest_semver_minor_comparison(self):
        expected_highest = "0.6.3"
        self.assertEqual(
            expected_highest,
            auto_semver.get_highest_tag_from_list(self.semver_list_minor)["semver"],
        )

    def test_get_highest_semver_major_comparison(self):
        expected_highest = "2.1.0"
        self.assertEqual(
            expected_highest,
            auto_semver.get_highest_tag_from_list(self.semver_list_major)["semver"],
        )

    def test_get_highest_semver_patch_comparison(self):
        expected_highest = "1.6.23"
        self.assertEqual(
            expected_highest,
            auto_semver.get_highest_tag_from_list(self.semver_list_patch)["semver"],
        )


if __name__ == "__main__":
    unittest.main()