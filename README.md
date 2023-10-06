# oci-queue-example-python

## setup
1. `python -m venv venv`
2. `. venv/bin/activate`
3. `pip install oci`

## channel-demo
1. set up your Instance Principal auth configuration for your oci tenancy (https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm)
2. replace `COMPARTMENT_ID`, `QUEUE_ENDPOINT`, `QUEUE_OCID` in channel-demo.py
3. `python channel-demo.py`
