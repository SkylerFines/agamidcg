def joint_snap():
    """
    Snap selected joints to the average position of selected vertices
    """
    joint_list = []
    vert_list = []

    # Get selection
    selection = cmds.ls(sl=True)

    # Check if there is a selection
    if not selection:
        return

    # Get object type
    for item in selection:
        object_type = cmds.objectType(item)

        if object_type == "joint":
            joint_list.append(item)

        elif "vtx" in item:
            mesh_name = item.split(".vtx[")[0]
            vert = item.split(".vtx[")[1].split("]")[0]
            if ":" in vert:
                start = vert.split(":")[0]
                end = vert.split(":")[1]
                for i in range(int(start), int(end) + 1):
                    vert = "{}.vtx[{}]".format(mesh_name, i)
                    vert_list.append(vert)
            else:
                vert_list.append(item)

    # Get the postion world space (verts)
    x_positions = []
    y_positions = []
    z_positions = []

    for vert in vert_list:
        position = cmds.xform(vert, query=True, translation=True, worldSpace=True)
        x_positions.append(position[0])
        y_positions.append(position[1])
        z_positions.append(position[2])

    # Get the average position (average position)
    average_x = sum(x_positions) / len(x_positions)
    average_y = sum(y_positions) / len(y_positions)
    average_z = sum(z_positions) / len(z_positions)

    # Move the joint to the average position
    for jnt in joint_list:
        cmds.xform(jnt, translation=[average_x, average_y, average_z], worldSpace=True)




