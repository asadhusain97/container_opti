# helper functions

# libraries needed
import yaml

#-------------------#
# logging functions #
#-------------------#

def load_log_configs(filepath='configs/logging.yaml'):
    with open(filepath, 'r') as file:
        log_yaml = yaml.safe_load(file)
    return log_yaml
