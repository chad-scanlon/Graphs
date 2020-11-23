def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     if path is None:
    #         path = [starting_vertex]
        
    #     if starting_vertex == destination_vertex:
    #         # print(path)
    #         return path

    #     for new_vertex in self.vertices[starting_vertex]:
    #         if new_vertex not in path:   
    #             new_path = path.copy()
    #             new_path.append(new_vertex)
    #             # print(new_path)
    #             value = self.dfs_recursive(new_vertex, destination_vertex, new_path)
    #             if value is not None:
    #                 return value