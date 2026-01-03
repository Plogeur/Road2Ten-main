import unittest
import simulation

# Website to generated test : https://felis-silvestris.lescigales.org/
class TestCrosing(unittest.TestCase):

    def setUp(self) :
        self.maxDiff = None # unittest parameter

        #                    id  sex   color  generation   root
        # dd_class.Dragodinde(1, "M", "Rousse", 1, self.genealogie_s1)

        # simple mono
        self.dd_sm1 = simulation.Dragodinde(100, "M", "Rousse", 1)
        self.dd_sm2 = simulation.Dragodinde(101, "F", "Amande", 1)

        # simple bi 
        self.dd_sb1 = simulation.Dragodinde(200, "M", "Indigo et Orchidée", 6)
        self.dd_sb2 = simulation.Dragodinde(201, "F", "Pourpre et Ivoire", 8)

        # simple bi 2 
        self.dd_sb3 = simulation.Dragodinde(202, "M", "Rousse et Amande", 2)
        self.dd_sb4 = simulation.Dragodinde(203, "F", "Rousse et Amande", 2)

        # first bi
        self.genealogie_1 = {0: ["Rousse et Dorée"], 1: ["Rousse","Dorée"]}
        self.dd_fb1 = simulation.Dragodinde(300, "M", "Rousse et Dorée", 2, self.genealogie_1)

        # second bi
        self.genealogie_2 = {0: ["Amande et Dorée"], 1: ["Amande","Dorée"]}
        self.dd_fb2 = simulation.Dragodinde(301, "F", "Amande et Dorée", 2, self.genealogie_2)

        # Mono Amande
        self.genealogie_3 = {0: ["Amande"], 1: ["Amande","Amande"], 2: ["Ebène","Amande"]}
        self.dd_1 = simulation.Dragodinde(1, "M", "Amande", 1, self.genealogie_3)

        # Mono Rousse
        self.genealogie_4 = {0: ["Rousse"], 1: ["Rousse","Rousse"], 2: ["Indigo","Rousse"]}
        self.dd_2 = simulation.Dragodinde(2, "F", "Rousse", 1, self.genealogie_4)

        # Bi Rousse et Amande
        self.genealogie_5 = {0: ["Rousse et Amande"], 1: ["Pourpre et Rousse","Amande et Indigo"],
                            2: ["Rousse et Prune","Ebène et Ivoire", "Indigo et Orchidée", "Amande et Turquoise"],
                            3 : ["Dorée et Orchidée", "Orchidée et Rousse", "Rousse et Ebène", "Turquoise et Rousse"]}
        self.dd_3 = simulation.Dragodinde(3, "M", "Rousse et Amande", 2, self.genealogie_5)

        # Bi Pourpre et Orchidée
        self.genealogie_6 = {0: ["Pourpre et Orchidée"], 1: ["Indigo et Ebène","Ivoire et Prune"],
                            2: ["Dorée et Emeraude","Orchidée et Emeraude", "Amande et Ivoire", "Indigo et Ivoire"], 
                            3 : ["Rousse et Ebène", "Turquoise et Rousse", "Rousse et Prune", "Dorée et Indigo"]}
        self.dd_4 = simulation.Dragodinde(4, "F", "Pourpre et Orchidée", 6, self.genealogie_6)

        # big ancester 
        self.genealogie_7 = {0: ["Amande"], 1: ["Amande","Amande"], 2: ["Amande","Amande", "Amande", "Amande"], 
                            3 : ["Amande", "Amande", "Amande", "Amande", "Amande", "Amande", "Amande", "Amande"]}
        self.dd_5 = simulation.Dragodinde(5, "M", "Amande", 1, self.genealogie_7)
 
        self.elevage = simulation.Elevage([self.dd_1, self.dd_2, self.dd_3, self.dd_4, self.dd_5,
                                         self.dd_sm1, self.dd_sm2, self.dd_sb1, self.dd_sb2,
                                         self.dd_fb1, self.dd_fb2, self.dd_sb3, self.dd_sb4])

    def uni_test_bad_crosing(self):
        with self.assertRaises(ValueError) as context:
            self.elevage.breeding(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(3))

        self.assertEqual(str(context.exception), "Cannot breed dragodindes of the same sex.")

    def test_crosing_big_ancestor_mono_mono(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(101), self.elevage.get_dd_by_id(5))
        expected_probability = {
                "Amande" : 100
            }
        
        #print("dic_probability big ancestor mono mono : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_mono_mono(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(2))
        expected_probability = {
                "Rousse": 41.019,
                "Amande": 41.019,
                "Rousse et Amande": 7.247,
                "Indigo": 4.337,
                "Ebène": 4.337,
                "Amande et Indigo": 0.957,
                "Rousse et Ebène": 0.957,
                "Indigo et Ebène": 0.128
            }

        #print("dic_probability mono-mono: ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)
    
    def test_crosing_mono_bi(self) :
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(1), self.elevage.get_dd_by_id(4))
        expected_probability = {
                "Amande" : 72.975,
                "Ebène": 8.391,
                "Pourpre et Orchidée": 6.191,
                "Indigo et Ebène": 4.592,
                "Ivoire et Prune": 1.47,
                "Indigo et Ivoire": 1.344,
                "Amande et Ivoire": 1.344,
                "Rousse et Ebène": 0.765,
                "Dorée et Indigo": 0.765,
                "Orchidée et Emeraude": 0.735,
                "Dorée et Emeraude": 0.735,
                "Turquoise et Rousse": 0.448,
                "Rousse et Prune": 0.245
            }

        #print("dic_probability mono-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)
    
    def test_crosing_bi_bi(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(3), self.elevage.get_dd_by_id(4))
        expected_probability = {
                "Rousse et Amande" : 16.595,
                "Pourpre et Orchidée" : 13.321,
                "Amande et Indigo" : 10.297,
                "Pourpre et Rousse" : 9.299,
                "Indigo et Ebène" : 8.513,
                "Indigo et Orchidée" : 4.649,
                "Ivoire et Prune" : 4.148,
                "Ebène et Ivoire" : 3.913,
                "Amande et Turquoise" : 3.913,
                "Rousse et Prune" : 3.378,
                "Indigo et Ivoire" : 3.234,
                "Rousse et Ebène" : 3.229,
                "Amande et Ivoire" : 3.234,
                "Turquoise et Rousse" : 2.382,
                "Orchidée et Emeraude" : 2.074,
                "Dorée et Emeraude" : 2.074,
                "Dorée et Orchidée" : 1.55,
                "Orchidée et Rousse" : 1.55,
                "Dorée et Indigo" : 1.513,
                "Pourpre" : 1.133

            }
        
        #print("dic_probability bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_mono_bi(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(100), self.elevage.get_dd_by_id(201))
        expected_probability = {
                "Rousse" : 83.333,
                "Pourpre et Ivoire" : 16.667
            }
        
        #print("dic_probability simple mono-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_mono_mono(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(100), self.elevage.get_dd_by_id(101))
        expected_probability = {
                "Rousse" : 45.455,
                "Amande" : 45.455,
                "Rousse et Amande" : 9.091
            }
        
        #print("dic_probability simple mono-mono : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_bi_bi(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(200), self.elevage.get_dd_by_id(201))
        expected_probability = {
                "Indigo et Orchidée" : 60.0,
                "Pourpre et Ivoire" : 40.0,
            }
        
        #print("dic_probability simple bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_simple_bi_bi2(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(202), self.elevage.get_dd_by_id(203))
        expected_probability = {
                "Rousse et Amande" : 100
            }
        
        #print("dic_probability simple bi-bi 2 : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

    def test_crosing_first_bi_bi(self):
        _, dic_probability = self.elevage.breeding(self.elevage.get_dd_by_id(300), self.elevage.get_dd_by_id(301))
        expected_probability = {
                "Rousse et Dorée" : 19.756,
                "Amande et Dorée" : 19.756,
                "Dorée" : 17.828,
                "Amande" : 17.549,
                "Rousse" : 17.549,
                "Ebène" : 6.887,
                "Rousse et Amande" : 0.676,
            }
        
        #print("dic_probability first bi-bi : ", dic_probability, '\n')
        self.assertEqual(dic_probability, expected_probability)

if __name__ == "__main__":
    unittest.main()