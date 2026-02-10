import traceback
import sys

try:
    import octobot_prediction_market.cli
    octobot_prediction_market.cli.main()
except Exception:
    traceback.print_exc()
except SystemExit as e:
    print(f"SystemExit: {e}")
