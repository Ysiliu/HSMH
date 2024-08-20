class Flow(object):
    def __init__(self,
        id: int,
        name: str,
        type: int,
        src: int,
        dst: int,
        size: int,
        period: int,
        deadline: int,
        jitter: int,):
        
        self.id = id
        self.name=name
        self.type=type # 流类型
        self.src = src #流发送端
        self.dst = dst #流接收端
        self.size = size
        self.period = period
        self.deadline = deadline
        self.jitter = jitter
        self.routing: Optional[Path] = None

    def rename(self, new_name):
        self.name = new_name

    @property
    def __str__(self):
        # return "["+self.name+"]"
        return "Flow [id = %d, name = %s]" % (self.id, self.name)

    @property
    def routing_path(self) -> Path:
        if self.routing is None:
            raise Exception("Route not set")
        return self._routing_path