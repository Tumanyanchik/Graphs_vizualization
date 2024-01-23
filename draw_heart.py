import plotly.graph_objs as go
import numpy as np

x = np.arange(-2, 2.001, 0.001)

def f_del_amour_top(x):
    return np.sqrt(1 - ((np.abs(x) - 1) ** 2))

def f_del_amour_bottom(x):
    return -2.5 * np.sqrt(1 - np.sqrt(np.abs(x) / 2))

frames = []
steps = 50  # Количество шагов анимации
for i in range(steps):
    step = 4 * (i+1)/steps
    x_top = np.arange(-2, -2 + step, 0.001)
    x_bottom = np.arange(2, 2 - step, -0.001)
    top_y = f_del_amour_top(x_top)  # Обновляем аргумент функции
    bottom_y = f_del_amour_bottom(x_bottom)  # Обновляем аргумент функции

    trace1 = go.Scatter(x=x, y=top_y, mode='lines+markers',
               name='<em>Your my heart</em>',
               marker=dict(
                    color=f_del_amour_top(x),
                    colorscale='YlOrRd', 
                    line=dict(
                        color=f_del_amour_top(x),
                        colorscale='YlOrRd'
                    ),
                    size=10*abs(f_del_amour_top(x))+5
                )
            )
    trace2 = go.Scatter(x=x_bottom, y=bottom_y, mode='lines+markers',
               name='<em>Your my soul</em>',
               marker=dict(
                    color=f_del_amour_bottom(x), 
                    colorscale='Hot', 
                    line=dict(
                        color=f_del_amour_bottom(x),
                        width=1.5,
                        colorscale='Hot'
                    )
                )
            )

    frames.append(go.Frame(data=[trace1, trace2], name=f'frame{i}'))

fig = go.Figure(
    data=[go.Scatter(x=[x[0]], y=[f_del_amour_top(x)[0]], mode='lines', name='<em>Your my heart</em>', line=dict(color='pink', width=2)),
          go.Scatter(x=[x[0]], y=[f_del_amour_bottom(x)[0]], mode='lines', name='<em>Your my soul</em>', line=dict(color='pink', width=2))],
    layout=go.Layout(title=dict(text="Graph", x=.52, xanchor="center"),
                     xaxis=dict(title="Values", range=[-4, 4], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink'),
                     yaxis=dict(title="Result", range=[-3, 2], zeroline=True, zerolinewidth=2, zerolinecolor='LightPink'),
                     updatemenus=[dict(type="buttons", buttons=[dict(label="►", method="animate", args=[None, {"frame": {"duration": 250, "redraw": True}, "fromcurrent": True}]),
                                                                dict(label="❚❚", method="animate", args=[[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}])])],
                     margin=dict(l=40, r=40, t=40, b=40), showlegend=False),
    frames=frames
)

fig.update_traces(hoverinfo="all", hovertemplate="Аргумент: %{x}<br>Функция: %{y}")
fig.show()