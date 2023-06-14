import java.util.ArrayList;
import java.util.List;

public class TreeNode {
    public int id;
    public TreeNode leftChild;
    public TreeNode rightChild;

    public TreeNode(int id, TreeNode left, TreeNode right) {
        this.id = id;
        this.leftChild = left;
        this.rightChild = right;
    }

    public TreeNode(int id) {
        this(id, null, null);
    }

    public boolean isLeaf() {
        return leftChild == null && rightChild == null;
    }

    public void print() {
        internalPrint(this, 0);
    }

    private void internalPrint(TreeNode node, int depth) {
        if (node == null) return;
        String indentation = "-".repeat(depth * 4);
        System.out.println(indentation + node.id);
        internalPrint(node.leftChild, depth + 1);
        internalPrint(node.rightChild, depth + 1);
    }

    public List<List<Integer>> paths() {
        return internalPaths(this);
    }

    private List<List<Integer>> internalPaths(TreeNode node) {
        if (node == null) {
            return List.of();
        }
        if (node.isLeaf()) {
            return List.of(List.of(node.id));
        }
        var pathsStartingFromLeftChild = internalPaths(node.leftChild);
        var pathsStartingFromRightChild = internalPaths(node.rightChild);
        var paths = new ArrayList<List<Integer>>();

        paths.addAll(pathsStartingFromLeftChild);
        paths.addAll(pathsStartingFromRightChild);

        List<List<Integer>> solution = new ArrayList<>();
        for (List<Integer> path : paths) {
            List<Integer> newPath = new ArrayList<>(path);
            newPath.add(0, node.id);
            solution.add(newPath);
        }

        return solution;
    }
}
