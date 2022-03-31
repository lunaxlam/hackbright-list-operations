import unittest
import list_operations


class ListSlicingTests(unittest.TestCase):
    """Tests for list slicing."""

    def test_head(self):
        result = list_operations.head(['Jan', 'Feb', 'Mar'])
        self.assertEqual(result, 'Jan')
    

    def test_tail(self):
        result = list_operations.tail(['Jan', 'Feb', 'Mar'])
        self.assertEqual(result, ['Feb', 'Mar'])


    def test_last(self):
        result = list_operations.last(['Jan', 'Feb', 'Mar'])
        self.assertEqual(result, 'Mar')
    

    def test_top(self):
        result = list_operations.top(['Jan', 'Feb', 'Mar'])
        self.assertEqual(result, ['Jan', 'Feb'])
    

    def test_first_three(self):
        result = list_operations.first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        self.assertEqual(result, ['Jan', 'Feb', 'Mar'])
    

    def test_last_five(self):
        result = list_operations.last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
        self.assertEqual(result, [15, 18, 21, 24, 27])
    

    def test_middle(self):
        result = list_operations.middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
        self.assertEqual(result, [6, 9, 12, 15, 18, 21])


    def test_inner_four(self):
        result = list_operations.inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
        self.assertEqual(result, [6, 9, 12, 15])
    

    def test_inner_four_end(self):
        result = list_operations.inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
        self.assertEqual(result, [12, 15, 18, 21])
    
    
    def test_replace_head(self):
        multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        list_operations.replace_head(multiples)
        self.assertEqual(multiples, [42, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    

    def test_replace_third_and_last(self):
        multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        list_operations.replace_third_and_last(multiples)
        self.assertEqual(multiples, [0, 3, 37, 9, 12, 15, 18, 21, 24, 37])
    

    def test_replace_middle(self):
        multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        list_operations.replace_middle(multiples)
        self.assertEqual(multiples, [0, 3, 42, 37, 24, 27])
    

    def test_delete_third_and_seventh(self):
        notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        list_operations.delete_third_and_seventh(notes)
        self.assertEqual(notes, ['Do', 'Re', 'Fa', 'So', 'La', 'Do'])
    

    def test_delete_middle(self):
        notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        list_operations.delete_middle(notes)
        self.assertEqual(notes, ['Do', 'Re', 'Ti', 'Do'])


if __name__ == "__main__":
    unittest.main()