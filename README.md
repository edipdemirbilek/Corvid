# Corvid

This programm does the following pipeline:
- gets Workjam Open Shift Apply and Open Shift Requests from SumoLogic Server,
- correlates Open Shift Apply with Open Shift Requests,
- enrich the user and shift information,
- adds the collected data to Dataset.

To run, it requires SumoLogic Access ID, Access Key, Target Workjam Environment, Workjam Public API username and password as programm arguments

## How to Run:

```console
python Corvid.py <SUMO_ACCESS_ID> <SUMO_ACCESS_KEY> <WJ_ENV> <WJ_USERNAME> <WJ_PASSWORD>
```
