def serializeProblem():
    class Node(object):
        def __init__(self, val: str, left = None, right = None):
            self.val = val
            self.left = left
            self.right = right
    
    def serialize(node: Node = None):
        if node is None:
            return 'None'
        
        result = "Node('{}', {}, {})".format(
            node.val.replace('\\', '\\\\').replace("'", "\\'"),
            serialize(node.left),
            serialize(node.right)
        )
        
        return result

    def deserialize(s: str = ''):
        result = eval(s)
        if isinstance(result, Node):
            return result
    
    return [Node, serialize, deserialize]

if __name__ == '__main__':
    funcs = serializeProblem()