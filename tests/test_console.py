#!/usr/bin/python3
"""console.py unittest"""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage, file_storage


class TestHBNBCommand(unittest.TestCase):
    """HBNB command unittest"""

    @classmethod
    def setUpClass(cls):
        """HBNBCommand setup for testing

        Temporarily rename any existing file.json.
        Reset FileStorage object dictionary.
        Create an instance of the command interpreter."""

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
            """Creating an instance of the HBNB command class,
            it allows the test
            methods within the class to access and use this
            instance during the testing process"""

            cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """HBNBCommand teardown testing

        Restores file.json and deletes test HBNBCommand instance
        """

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary"""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Deletes any created file.json"""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_create_for_errors(self):
        """Tests the create command errors"""

        # Test if class name is missing
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Tests if class doesn't exists
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create asdfsfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

    def test_create_command_validity(self):
        """Test that create command"""
        # Creates BaseModel instance and saves its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()

        # creates user instance and saves ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            u = f.getvalue().strip()

        # creates State instance and saves ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()

        # create Place instance and saves ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            pl = f.getvalue().strip()

        # creates City instance and saves ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            ct = f.getvalue().strip()

        # create Review instance and saves ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rv = f.getvalue().strip()

        # create Amenity instance and saves its ID
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()

        # Tests if created instances are in the output of 'all' command
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(u, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(st, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            self.assertIn(pl, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            self.assertIn(ct, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Review")
            self.assertIn(rv, f.getvalue())

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Amenity")
            self.assertIn(am, f.getvalue())

    def test_create_command_with_kwargs(self):
        """Test create command with kwargs"""

        # Test create command with additional key-value pair
        with patch("sys.stdout", new=StringIO()) as f:
            call = (f'create Place city_id="0001" name="My_house"
                    number_rooms=4 latitude=37.77 longitude=43.434')
            self.HBNB.onecmd(call)
            pl = f.getvalue().strip()

        # Tests if the created instance and kwargs
        # are in the output of 'all' command

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            output = f.getvalue()
            self.assertIn(pl, output)
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'name': ''My house", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'latitude': 37.77", output)
            self.assertIn("'longitude': 43.434", output)

    if __name__ == "__main__":
        unittest.main()
