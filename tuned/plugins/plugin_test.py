import tuned.monitors

class TestPlugin(tuned.plugins.Plugin):
	def __init__(self, devices = None, options = None):
		"""
		"""
		super(self.__class__, self).__init__(options)

		self._monitors = [
			tuned.monitors.get_repository().create("load", None),
			tuned.monitors.get_repository().create("disk", None)
		]

	def cleanup(self):
		for monitor in self._monitors:
			tuned.monitors.get_repository().delete(monitor)

	def update_tuning(self):
		pass
