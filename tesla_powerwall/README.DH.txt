Prereuisites:

- install "requests" and "responses" 
--> pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org requests
--> pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org responses

- setup environment:
-- setup_environment.batteries

- run unit tests from code:
-- should be able to "autodiscover" the tests but its not working  (likely a pythonpath issue)
--> Failed to import test module: unit.test_powerwall
Traceback (most recent call last):
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2544.0_x64__qbz5n2kfra8p0\lib\unittest\loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2544.0_x64__qbz5n2kfra8p0\lib\unittest\loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "c:\src\solar\tesla_powerwall\tests\unit\test_powerwall.py", line 4, in <module>
    import responses
ModuleNotFoundError: No module named 'responses'





- run sample program to show data:

C:\src\solar\tesla_powerwall>python3 examples\example.py 
Home Energy Gateway:

        Charge (%): 94
          Capacity: 13681
    Nominal Energy: 12857
       Grid Status: SystemGridConnected
Backup Reserve (%): 34
       Device Type: teg
  Software Version: 23.12.10


   Meter    Power   Energy exported   Energy imported   Active Drawing from   Sending to
    site   -0.009            2617.2            3095.9    False        False        False
 battery    -2.76            4443.9            4979.7     True        False         True
    load     1.45               0.0           11456.1     True        False         True
   solar    4.197           11539.8              26.6     True         True        False


   Meter    Current-A    Current-B    Current-C  RealPower-A  RealPower-B  RealPower-C    Voltage-1    Voltage-2    Voltage-3
    site         5.74         4.62         1.09         1339        -1100         -246       237.89       241.13       239.44