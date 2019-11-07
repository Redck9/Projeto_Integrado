from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

NODE, EDGE, ATTR = range(3)

Attrs = Dict[str, str]

DslAttr = Tuple[int, int, str, str]
DslNode = Tuple[int, str, Attrs]
DslEdge = Tuple[int, str, str, Attrs]
DslGraph = Iterable[Union[DslAttr, DslNode, DslEdge]]


class Node:  # pylint: disable=too-few-public-methods

    """
    Simple implementation of a Node in our Graphviz-like DSL.
    """

    def __init__(self, name: str, attrs: Optional[Attrs] = None) -> None:
        self.name = name
        self.attrs = attrs or {}

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Node):
            return self.name == other.name and self.attrs == other.attrs
        return NotImplemented


class Edge:  # pylint: disable=too-few-public-methods
    """
    Simple implementation of an Edge in our Graphviz-like DSL.
    """

    def __init__(self, src: Node, dst: Node, attrs: Optional[Attrs] = None) -> None:
        self.src = src
        self.dst = dst
        self.attrs = attrs or {}

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Edge):
            return (
                self.src == other.src
                and self.dst == other.dst
                and self.attrs == other.attrs
            )
        return NotImplemented


class Graph:  # pylint: disable=too-few-public-methods
    """
    Simple implementation of a Graph in our Graphviz-like DSL.
    """

    def __init__(self, data: Optional[DslGraph] = None):
        self.nodes: List[Node] = []
        self.edges: List[Edge] = []
        self.attrs: Dict[str, Attrs] = {}
        data = data or []
        if not isinstance(data, list):
            raise TypeError("Graph expects a list!")
        for item in data:
            try:
                operator, *args = item
            except ValueError:
                raise TypeError("Malformed data item!")
            if not args:
                raise TypeError("Malformed operation!")
            if operator == NODE:
                name, attrs = args
                self.nodes.append(Node(name, attrs))
            elif operator == EDGE:
                src, dst, attrs = args
                self.edges.append(Edge(src, dst, attrs))
            elif operator == ATTR:
                key, val = args
                self.attrs[key] = val
            else:
                raise ValueError("Unsupported operation!")