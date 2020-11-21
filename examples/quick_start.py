import pygrading as gg

job = gg.Job()

job.verdict("Accept")
job.score(100)
job.comment("Hello World")

job.print()
