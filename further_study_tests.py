import unittest
import further_study


class FurtherStudyTests(unittest.TestCase):
    """Tests for list slicing further study."""


    def test_custom_len(self):
        result = further_study.custom_len(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
        self.assertEqual(result, 8)
    

    def test_custom_append(self):
        notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        further_study.custom_append(notes, 'Re')
        self.assertEqual(notes, ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do', 'Re'])


    def test_custom_extend(self):
        months = ['Jan', 'Feb', 'Mar']
        further_study.custom_extend(months, ['Apr', 'May'])
        self.assertEqual(months, ['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    

    def test_custom_insert(self):
        months = ['Jan', 'Mar']
        further_study.custom_insert(months, 1, 'Feb')
        self.assertEqual(months, ['Jan', 'Feb', 'Mar'])
    

    def test_custom_remove(self):
        notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        further_study.custom_remove(notes, 'Do')
        self.assertEqual(notes, ['Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'])
    

    def test_custom_pop(self):
        months = ['Jan', 'Feb', 'March']
        result = further_study.custom_pop(months)
        self.assertEqual(result, 'March')
        self.assertEqual(months, ['Jan', 'Feb'])


    def test_custom_index(self):
        result = further_study.custom_index(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Re')
        self.assertEqual(result, 1)


    def test_custom_count(self):
        result = further_study.custom_count(['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do'], 'Do')
        self.assertEqual(result, 2)
    
    
    def test_custom_reverse(self):
        multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
        result = further_study.custom_reverse(multiples)
        self.assertEqual(result, [27, 24, 21, 18, 15, 12, 9, 6, 3, 0])
    

    def test_custom_contains(self):
        result = further_study.custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 23)
        self.assertEqual(result, False)
        
        result2 = further_study.custom_contains([0, 3, 6, 9, 12, 15, 18, 21, 24], 24)
        self.assertEqual(result2, True)
    

    def test_custom_equality(self):
        result = further_study.custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Feb', 'Mar'])
        self.assertEqual(result, True)

        result2 = further_study.custom_equality(['Jan', 'Feb', 'Mar'], ['Jan', 'Mar', 'Feb'])
        self.assertEqual(result2, False)


if __name__ == "__main__":
    unittest.main()