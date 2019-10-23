from collections import deque, namedtuple
import sys
import json

# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

start = sys.argv[1]
destination = sys.argv[2]

def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )
      
    def printOnThis()
      print("keep going")
      return 0
    #made changes now
    
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex
        
        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        path.append(distances[dest])
        return path


graph = Graph([
    ("1", "2", 27), ("2", "3",180 ),("3","4",40),("3","78",140),
    ("4","5",120),("5","12",130),("12","13",71),("13","14",230),
    ("14","15",68),("78","13",140),("5","6",25),("6","7",18),("7","8",35),("8","9",55),("9","10",170)
    ,("9","37",290),("32","37",61),("32","31",120),("32","83",48),("83","33",37),("31","33",34)
    ,("31","29",38),("29","28",34),("26","28",44),("26","27",5),("26","79",87),("79","24",87),
    ("24","25",17),("23","24",80),("22","23",16),("21","22",56),("19","22",30),("19","20",22),("16","19",71),
    ("16","17",68),("17","18",29),("29","30",90),("30","34",76),("34","35",51),("35","36",31),
    ("32","36",85),("36","38",61),("38","39",60),("38","40",110),("40","41",140),("40","55",160),("38","42",32),("42","43",10),
    ("42","48",17),("48","50",87),("37","50",22),("48","46",19),("46","44",38),("44","45",12),("48","49",49),
    ("49","47",30),("49","51",27),("51","52",25),("52","54",65),("54","56",36),("56","57",10),("56","59",38),
    ("59","58",28),("58","55",75),("52","53",41),("53","60",30),("60","84",9),("61","84",48),
    ("82","61",50),("71","82",66),("81","71",19),("71","73",40),("71","72",18),("72","74",120),
    ("74","75",30),("75","76",10),("81","69",40),("61","69",58),("61","62",12),("69","68",41),
    ("77","68",74),("68","80",58),("80","67",15),("67","63",50),("62","63",30),("63","58",61),
    ("58","64",42),("65","64",38),("65","66",47),("67","66",23),("31","83",62),("70","81",8),
    ("2","1",27),("3","2",180),("4","3",),("78","3",140),("5","4",120),("12","5",130),("13","12",71),("14","13",230),("15","14",68),("13","78",140,),
    ("6","5",25),("7","6",18),("8","7",35),("9","8",55),("10","9",170),("37","9",290),("37","32",61),("31","32",120),("83","32",48),("33","83",37),
    ("33","31",34),("29","31",38),("28","29",34),("28","26",44),("27","26",5),("79","26",87),("24","79",87),("25","24",17),("24","23",80),("23","22",16),
    ("22","21",56),("22","19",30),("20","19",22),("19","16",71),("17","16",68),("18","17",29),("30","29",90),("34","30",76),("35","34",51),("36","35",31),
    ("36","32",85),("38","36",61),("39","38",60),("40","38",110),("41","40",140),("55","40",160),("42","38",32),("43","42",10),("48","42",17),("50","48",87),
    ("50","37",22),("46","48",19),("44","46",38),("45","44",12),("49","48",49),("47","49",30),("51","49",27),("52","51",25),("54","52",65),("56","54",36),
    ("57","56",10),("59","56",38),("58","59",28),("55","58",75),("53","52",41),("60","53",30),("84","60",9),("84","61",48),("61","82",50),("82","71",66),
    ("71","81",19),("73","71",40),("72","71",18),("74","72",120),("75","74",30),("76","75",10),("69","81",40),("69","61",58),("62","61",12),("68","69",41),
    ("68","77",74),("80","68",58),("67","80",15),("63","67",50),("63","62",30),("58","63",61),("64","58",42),("64","65",38),("66","65",47),("66","67",23),
    ("83","31",62),("81","70",8)
])
relate = {"1" : [12.975467, 79.160537],
          "2" : [12.975310, 79.159765],
          "3" : [12.973756, 79.159602],
          "4":[12.973683, 79.159246],
          "5":[12.972596, 79.159171],
          "6":[12.972567, 79.158951],
          "7":[12.972577, 79.158784],
          "8":[12.972274, 79.158698],
          "9":[12.972013, 79.158322],
          "10":[12.972044, 79.156788],
          "11":[12.971866, 79.156791],
          "12":[12.972551, 79.160340],
          "13":[12.972572, 79.160984],
          "14":[12.972908, 79.163079],
          "15":[12.973017, 79.163709],
          "16":[12.971851, 79.164288],
          "17":[12.971266, 79.164438],
          "18":[12.971214, 79.165345],
          "19":[12.971742, 79.163644],
          "20":[12.971474, 79.163667],
          "21":[12.971304, 79.163536],
          "22":[12.971669, 79.163210],
          "23":[12.971648, 79.163062],
          "24":[12.971525, 79.162327],
          "25":[12.971125, 79.162407],
          "26":[12.971331, 79.160765],
          "27":[12.971010, 79.160867],
          "28":[12.971271, 79.160363],
          "29":[12.971195, 79.160052],
          "30":[12.970394, 79.160139],
          "31":[12.971131, 79.159709],
          "32":[12.971000, 79.158700],
          "33":[12.970974, 79.159446],
          "34":[12.970237, 79.159451],
          "35":[12.970240, 79.158979],
          "36":[12.970235, 79.158689],
          "37":[12.970754, 79.158259],
          "38":[12.969693, 79.158657],
          "39":[12.969573, 79.159384],
          "40":[12.968700, 79.158646],
          "41":[12.967472, 79.158618],
          "42":[12.969696, 79.158363],
          "43":[12.969526, 79.158363],
          "44":[12.969210, 79.158248],
          "45":[12.969032, 79.158245],
          "46":[12.969503, 79.158083],
          "47":[12.969257, 79.157726],
          "48":[12.969725, 79.158144],
          "49":[12.969730, 79.157627],
          "50":[12.970573, 79.158176],
          "51":[12.969636, 79.157399],
          "52":[12.969641, 79.157155],
          "53":[12.969662, 79.156782],
          "54":[12.969045, 79.157160],
          "55":[12.968802, 79.157157],
          "56":[12.969123, 79.156840],
          "57":[12.969345, 79.156851],
          "58":[12.968817, 79.156465],
          "59":[12.969063, 79.156497],
          "60":[12.969675, 79.156489],
          "61":[12.969696, 79.155923],
          "62":[12.969304, 79.155907],
          "63":[12.968800, 79.155907],
          "64":[12.968544, 79.156211],
          "65":[12.968429, 79.155894],
          "66":[12.968630, 79.155527],
          "67":[12.968808, 79.155447],
          "68":[12.969310, 79.155297],
          "69":[12.969681, 79.155310],
          "70":[12.969997, 79.155697],
          "71":[12.970214, 79.155335],
          "72":[12.970363, 79.155295],
          "73":[12.970224, 79.155008],
          "74":[12.970409, 79.154209],
          "75":[12.970179, 79.154209],
          "76":[12.970167, 79.154339],
          "77":[12.969334, 79.154634],
          "78":[12.973779, 79.160927],
          "79":[12.971437, 79.161558],
          "80":[12.968787, 79.155285],
          "81":[12.970044, 79.155324],
          "82":[12.970190, 79.155946],
          "83":[12.971070, 79.159142],
          "84":[12.969660, 79.156422]
          }

y = {}
y["path"] = list(graph.dijkstra(start, destination))
y["dist"] = y["path"][len(y["path"])-1]
del y["path"][len(y["path"])-1]
for i in range(len(y["path"])):
    y["path"][i] = relate[y["path"][i]]
print(json.dumps(y))
sys.stdout.flush()
