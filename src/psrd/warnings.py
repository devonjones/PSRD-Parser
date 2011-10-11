import sys

class WarningReporting():
	def __init__(self):
		self.context = None
		self.book = None

	def __call__(self):
		return self

	def report(self, string):
		sys.stderr.write("%s (%s): %s\n" % (self.book, self.context, string))

WarningReporting = WarningReporting()
