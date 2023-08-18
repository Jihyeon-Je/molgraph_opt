import numpy as np
import plotly.graph_objects as go

def draw_mol(mol, x,y,z, atoms, mask=None):
    color_map = {'C': 'lemonchiffon',
             'O': 'lightblue',
             'N': 'lavender',
             'S': 'lightcyan',
             'H': 'lightgreen',
             'F': 'orange'} 
    

    color_code=[]
    for i in range(len(atoms)):
        color_code.append(color_map[atoms[i]])

    x_edges_1 = []
    y_edges_1 = []
    z_edges_1 = []

    x_edges_2 = []
    y_edges_2 = []
    z_edges_2 = []
    
    x_edges_3 = []
    y_edges_3 = []
    z_edges_3 = []
    
    x_mask = []
    y_mask = []
    z_mask = []

    x_mask_node = []
    y_mask_node = []
    z_mask_node = []
    
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            p1 = np.array([x[i], y[i], z[i]])
            p2 = np.array([x[j], y[j], z[j]])
            if mol.GetBondBetweenAtoms(i,j) is not None:
                edge = str(mol.GetBondBetweenAtoms(i,j).GetBondType())
            else: edge = 'zero'
            
            draw_edge_int = 0
            if edge == 'SINGLE': 
                draw_edge_int = 1
            elif edge == 'DOUBLE': 
                draw_edge_int = 2
            elif edge == 'TRIPLE': 
                draw_edge_int = 3
            
            if mask is not None:
                for k in range(len(mask)):
                    x_mask_node.append(x[mask[k]])
                    y_mask_node.append(y[mask[k]])
                    z_mask_node.append(z[mask[k]])
                if (i in mask or j in mask) & (draw_edge_int!=0):
                    x_coors = [p1[0],p2[0],None]
                    x_mask += x_coors
                    y_coors = [p1[1],p2[1],None]
                    y_mask += y_coors
                    z_coors = [p1[2],p2[2],None]
                    z_mask += z_coors
            if draw_edge_int==1:
                x_coors = [p1[0],p2[0],None]
                x_edges_1 += x_coors
                y_coors = [p1[1],p2[1],None]
                y_edges_1 += y_coors
                z_coors = [p1[2],p2[2],None]
                z_edges_1 += z_coors
            elif draw_edge_int==2:
                x_coors = [p1[0],p2[0],None]
                x_edges_2 += x_coors
                y_coors = [p1[1],p2[1],None]
                y_edges_2 += y_coors
                z_coors = [p1[2],p2[2],None]
                z_edges_2 += z_coors
            elif draw_edge_int==3:
                x_coors = [p1[0],p2[0],None]
                x_edges_3 += x_coors
                y_coors = [p1[1],p2[1],None]
                y_edges_3 += y_coors
                z_coors = [p1[2],p2[2],None]
                z_edges_3 += z_coors
    #create a trace for the nodes
    trace_nodes = go.Scatter3d(x=x,
                            y=y,
                            z=z,
                            mode='markers',
                            marker=dict(symbol='circle',
                                        size=10,
                                        color=color_code,
                                        line=dict(color='black', width=0.5)),
                            text=atoms,
                            hoverinfo='text')
    mask_nodes = go.Scatter3d(x=x_mask_node,
                            y=y_mask_node,
                            z=z_mask_node,
                            mode='markers',
                            marker=dict(symbol='circle',
                                        size=10,
                                        color='lightsalmon'
                                        ),
                            text=atoms,
                            hoverinfo='text')
    mask_edges = go.Scatter3d(x=x_mask,
                        y=y_mask,
                        z=z_mask,
                        mode='lines',
                        line=dict(color='lightsalmon', width=20),
                        hoverinfo='none'
)
    trace_edges1 = go.Scatter3d(x=x_edges_1,
                        y=y_edges_1,
                        z=z_edges_1,
                        mode='lines',
                        line=dict(color='grey', width=10),
                        hoverinfo='none'
)
    trace_edges2 = go.Scatter3d(x=x_edges_2,
                    y=y_edges_2,
                    z=z_edges_2,
                    mode='lines',
                    line=dict(color='darkgrey', width=11),
                    hoverinfo='none'
)
    trace_edges3 = go.Scatter3d(x=x_edges_3,
                y=y_edges_3,
                z=z_edges_3,
                mode='lines',
                line=dict(color='black', width=12),
                hoverinfo='none'
)
    
    #we need to set the axis for the plot 
    axis = dict(showbackground=False,
                showline=True,
                zeroline=False,
                showgrid=True,
                showticklabels=False,
                title='')
    #also need to create the layout for our plot
    layout = go.Layout(
                    width=650,
                    height=625,
                    showlegend=False,
                    scene=dict(xaxis=dict(axis),
                            yaxis=dict(axis),
                            zaxis=dict(axis),
                            ),
                    margin=dict(t=100),
                    hovermode='closest')
    
    #Include the traces we want to plot and create a figure
    data = [trace_nodes, mask_nodes, mask_edges, trace_edges1, trace_edges2, trace_edges3]
    fig = go.Figure(data=data, layout=layout)

    fig.show()


import numpy as np
import plotly.graph_objects as go

