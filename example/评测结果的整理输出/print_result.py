import pygrading.general_test as gg


def postwork(job):
    job.verdict("Accept")
    job.score(100)
    job.detail("Detail Message!")
    job.custom("custom_key", "custom_value")


myjob = gg.job(prework=None, run=None, postwork=postwork)

myjob.start()

myjob.print()
