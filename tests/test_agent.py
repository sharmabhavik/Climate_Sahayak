# === tests/test_agent.py ===
import unittest
from agent.agent_graph import climate_agent

class TestClimateAgent(unittest.TestCase):
    def test_basic_query(self):
        """
        Simulates a full agent query and checks required outputs are generated.
        """
        query = "What will be the climate impact in India in 2050?"
        result = climate_agent.invoke({"query": query})
        self.assertIn("predicted_temperature", result)
        self.assertIn("policy_suggestions", result)
        self.assertIn("result", result)
        self.assertIsInstance(result["predicted_temperature"], float)
        self.assertTrue("###" in result["result"])  # markdown format

    def test_missing_query(self):
        """
        Should raise an error if query is missing.
        """
        with self.assertRaises(ValueError):
            climate_agent.invoke({})

if __name__ == "__main__":
    unittest.main()
