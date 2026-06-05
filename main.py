class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def preorder(root) -> list:
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root) -> list:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root) -> list:
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


def level_order(root) -> list:
    if not root:
        return []
    
    result = []
    queue = [root] 
    
    while queue:
        level_size = len(queue) 
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)  
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result
def left_view(root) -> list:
    levels = level_order(root)
    return [level[0] for level in levels]
if __name__ == "__main__":

    
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.right = Node(5)
    root1.right.right = Node(6)

    print("=== ТЕСТ 1 ===")
    print(f"Прямой обход (Preorder):     {preorder(root1)}")
    print(f"Симметричный (Inorder):      {inorder(root1)}")
    print(f"Обратный обход (Postorder):   {postorder(root1)}")
    print(f"По уровням (Level order):    {level_order(root1)}")
    print(f"Левый вид (Left View):       {left_view(root1)}")

    print("\n" + "="*40 + "\n")

    root2 = Node(5)
    root2.left = Node(10)
    root2.left.right = Node(20)
    root2.left.right.left = Node(30)

    print("=== ТЕСТ 2 ===")
    print(f"Прямой обход (Preorder):     {preorder(root2)}")
    print(f"Симметричный (Inorder):      {inorder(root2)}")
    print(f"Обратный обход (Postorder):   {postorder(root2)}")
    print(f"По уровням (Level order):    {level_order(root2)}")
    print(f"Левый вид (Left View):       {left_view(root2)}")
