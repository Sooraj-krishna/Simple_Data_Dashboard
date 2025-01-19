import unittest
import pandas as pd
from io import StringIO

# Sample data for testing
SAMPLE_CSV = """
Name,Age,Department,Salary
Alice,30,HR,50000
Bob,25,Engineering,60000
Charlie,35,HR,70000
Dave,40,Engineering,80000
"""

def filter_data(df, column, value):
    """Filters the DataFrame based on a column and value."""
    return df[df[column] == value]

class TestAppFunctions(unittest.TestCase):

    def setUp(self):
        """Set up a DataFrame for testing."""
        self.df = pd.read_csv(StringIO(SAMPLE_CSV))

    def test_filter_data_valid(self):
        """Test filtering with valid data."""
        filtered_df = filter_data(self.df, 'Department', 'HR')
        self.assertEqual(len(filtered_df), 2)  # Expect 2 rows
        self.assertTrue((filtered_df['Name'] == ['Alice', 'Charlie']).all())

    def test_filter_data_invalid_column(self):
        """Test filtering with an invalid column."""
        with self.assertRaises(KeyError):
            filter_data(self.df, 'InvalidColumn', 'HR')

    def test_filter_data_no_match(self):
        """Test filtering with a value that has no matches."""
        filtered_df = filter_data(self.df, 'Department', 'Marketing')
        self.assertTrue(filtered_df.empty)

    def test_filter_data_numeric(self):
        """Test filtering on numeric data."""
        filtered_df = filter_data(self.df, 'Age', 30)
        self.assertEqual(len(filtered_df), 1)  # Expect 1 row
        self.assertEqual(filtered_df.iloc[0]['Name'], 'Alice')

if __name__ == "__main__":
    unittest.main()
