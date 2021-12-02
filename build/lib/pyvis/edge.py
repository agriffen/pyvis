class Edge(object):

    def __init__(self, source, dest, group, directed=False, **options):
        self.options = options
        self.options['from'] = source
        self.options['to'] = dest
        self.options['group'] = group
        if directed:
            self.options["arrows"] = "to"
