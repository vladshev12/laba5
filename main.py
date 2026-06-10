class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)         
        preorder(root.left, result)         
        preorder(root.right, result)       
    return result

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)   
        result.append(root.value)         
        inorder(root.right, result)    
    return result

def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)     
        postorder(root.right, result)      
        result.append(root.value)           
    return result

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = [root] 
    
    while queue:
        level_size = len(queue) 
        current_level = []
        
        for i in range(level_size):
            node = queue.pop(0)  
            current_level.append(node.value) 
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result

def left_view(root):
    levels = level_order(root)
    return [level[0] for level in levels]


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.right = TreeNode(6)

print("   ТЕСТ 1 ")
print(f"Прямой обход (Preorder):     {preorder(root1, [])}")
print(f"Симметричный (Inorder):      {inorder(root1, [])}")
print(f"Обратный обход (Postorder):   {postorder(root1, [])}")
print(f"По уровням (Level order):    {level_order(root1)}")
print(f"Левый вид (Left View):       {left_view(root1)}")

print("\n")
root2 = TreeNode(5)
root2.left = TreeNode(10)
root2.left.right = TreeNode(20)
root2.left.right.left = TreeNode(30)

print("    ТЕСТ 2")
print(f"Прямой обход (Preorder):     {preorder(root2, [])}")
print(f"Симметричный (Inorder):      {inorder(root2, [])}")
print(f"Обратный обход (Postorder):   {postorder(root2, [])}")
print(f"По уровням (Level order):    {level_order(root2)}")
print(f"Левый вид (Left View):       {left_view(root2)}")
