import unittest
import theLED.Grid as Grid
import theLED.Instructions as Instructions
import theLED.Modification as Modification
import theLED.Links as Links

class MyTest(unittest.TestCase):
    #Grid
    def test_gridInputRemoveLeftWhiteSpace(self):
        self.assertEqual(Grid.gridInputRemoveLeftWhiteSpace("   4"), ['4'])
        self.assertEqual(Grid.gridInputRemoveLeftWhiteSpace("   3"), ['3'])
        self.assertNotEqual(Grid.gridInputRemoveLeftWhiteSpace("   3"), [' 3'])
        self.assertNotEqual(Grid.gridInputRemoveLeftWhiteSpace("   3"), ['h'])
       
    def test_gridCheckLength(self):
        self.assertTrue(Grid.gridCheckLength([1]))
        self.assertFalse(Grid.gridCheckLength([1, 2]))
        
    def test_generateGrid(self):
        self.assertEqual(Grid.Grid(1).grid, {(0, 0): False, (0, 1): False, (1, 0): False, (1, 1): False})
        self.assertNotEqual(Grid.Grid(1).grid, {(0, 0): True, (0, 1): True, (1, 0): False, (1, 1): False})
    
    #Instructions
    def test_instructionFormat(self):
        self.assertEqual(Instructions.instructionFormat("turn on 25, 28 through 80,200"), ['on', '25', '28', '80', '200'])
        
    def test_instructionValidTypes(self):
        #length
        self.assertTrue(Instructions.instructionValidTypes(['on', '25', '28', '80', '200'])) #OK
        self.assertFalse(Instructions.instructionValidTypes(['on', '25', '28', '80', '200', "300"])) #long
        self.assertFalse(Instructions.instructionValidTypes(['on', '25', '28', '80'])) #short
        #commands
        self.assertTrue(Instructions.instructionValidTypes(['on', '25', '28', '80', '200']))
        self.assertTrue(Instructions.instructionValidTypes(['off', '25', '28', '80', '200']))
        self.assertTrue(Instructions.instructionValidTypes(['switch', '25', '28', '80', '200']))
        self.assertFalse(Instructions.instructionValidTypes(['son', '25', '28', '80', '200']))
        self.assertFalse(Instructions.instructionValidTypes(['On', '25', '28', '80', '200']))
        self.assertFalse(Instructions.instructionValidTypes([' on', '25', '28', '80', '200']))
        #generate_integers
        self.assertFalse(Instructions.instructionValidTypes(['on', 'ted', '28', '80', '200']))
        self.assertFalse(Instructions.instructionValidTypes(['on', '25', 'fred', '80', '200']))
        self.assertFalse(Instructions.instructionValidTypes(['on', '25', '28', 'lead', '200']))
        self.assertFalse(Instructions.instructionValidTypes(['on', '25', '28', '80', 'bed']))
        
    def test_Instruction(self):
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).instruction, ["switch", 1, 2, 3, 4])
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).command, "switch")
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).start, (1, 2))
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).end, (3, 4))
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).x1, 1)
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).y1, 2)
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).x2, 3)
        self.assertEqual(Instructions.Instruction(["switch", 1, 2, 3, 4]).y2, 4)
        
    #Modification
    def test_modificationEntry(self):
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["on", 1, 2, 3, 4]), True), True)
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["off", 1, 2, 3, 4]), True), False)
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["on", 1, 2, 3, 4]), False), True)
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["off", 1, 2, 3, 4]), False), False)
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["switch", 1, 2, 3, 4]), True), False)
        self.assertEqual(Modification.modificationEntry(Instructions.Instruction(["switch", 1, 2, 3, 4]), False), True)
        
    def test_modificationGrid(self):
        instructionList = ["switch", 1, 1, 2, 2]
        inputInstruction = Instructions.Instruction(instructionList)
        inputGrid = {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): False, (1, 2): False, (2, 0): False, (2, 1): False, (2, 2): False}
        outputGrid = {(0, 0): False, (0, 1): False, (0, 2): False, (1, 0): False, (1, 1): True, (1, 2): True, (2, 0): False, (2, 1): True, (2, 2): True}
        self.assertEqual(Modification.modificationGrid(inputInstruction, inputGrid), outputGrid)
    
    #Links
    def test_validLink(self):
        self.assertTrue(Links.validLink("http://www.google.com"))
        self.assertFalse(Links.validLink("thisWillNotWork$$$%$%$%$"))
        
    def test_createLinkList(self):
        self.assertEqual(Links.createLinkList("LinksSource.txt"), ['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt', 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a_v2.txt', 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b_v2.txt', 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt', 'http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt'])    