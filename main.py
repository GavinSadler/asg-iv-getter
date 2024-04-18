import dearpygui.dearpygui as dpg
from dearpygui.demo import show_demo
import themes
import numpy as np

dpg.create_context()

# show_demo()

# dpg.show_style_editor()
# dpg.show_font_manager()

with dpg.font_registry():
    default_font = dpg.add_font(f"./NotoSans-Regular.ttf", 18)
    # default_font = dpg.add_font(f"./NotoSans-Medium.ttf", 18)
    # default_font = dpg.add_font(f"./NotoSans-Bold.ttf", 18)

# Show the light theme
dpg.bind_theme(themes.create_theme_imgui_light())

# Bind the custom font
dpg.bind_font(default_font)

with dpg.window(tag="main_window"):

    # with dpg.menu_bar():
    #     with dpg.menu(label="File"):
    #         dpg.add_menu_item(label="Hello there")

    with dpg.tab_bar():

        # === New Measurement Tab ===
        with dpg.tab(label="New Measurement"):

            with dpg.group(horizontal=True):

                with dpg.group():

                    child_width = 325
                    input_width = 50

                    # === Measurement Configuration Layout ===
                    with dpg.child_window(width=child_width, height=250):
                        with dpg.group():
                            dpg.add_text("Measurement Configuration")
                            dpg.add_separator()
                            dpg.add_input_text(decimal=True, label="Voltage Start", default_value=-1.5, width=input_width)
                            dpg.add_input_text(decimal=True, label="Voltage Step", default_value=0.01, width=input_width)
                            dpg.add_input_text(decimal=True, label="Voltage End", default_value=1.5, width=input_width)
                            dpg.add_separator()
                            dpg.add_input_text(decimal=True, label="Compliance (A)", default_value=0.02, width=input_width)
                            dpg.add_input_text(decimal=True, label="Pause Between Measurements (s)", default_value=0.01, width=input_width)
                            dpg.add_input_text(decimal=True, label="Number of Measurements", default_value=3, width=input_width)
                            dpg.add_button(label="Run Measurement", width=-1, enabled=False)

                    # === Quick Test Configuration Layout ====
                    with dpg.child_window(width=child_width, height=225):
                        with dpg.group():
                            dpg.add_text("Quick Test Configuration")
                            dpg.add_separator()
                            dpg.add_input_text(decimal=True, label="Voltage Start", default_value=-1.5, width=input_width)
                            dpg.add_input_text(decimal=True, label="Voltage Step", default_value=0.01, width=input_width)
                            dpg.add_input_text(decimal=True, label="Voltage End", default_value=1.5, width=input_width)
                            dpg.add_separator()
                            dpg.add_input_text(decimal=True, label="Compliance (A)", default_value=0.02, width=input_width)
                            dpg.add_input_text(decimal=True, label="Pause Between Measurements (s)", default_value=0.01, width=input_width)
                            dpg.add_button(label="Run Quick Test", width=-1, enabled=False)

                    with dpg.child_window(width=child_width, height=130):
                        dpg.add_text("Test Device Connections")
                        dpg.add_separator()
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="Connect")
                            dpg.add_text("Source Meter 1: ")
                            dpg.add_text("Disconnected")
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="Connect")
                            dpg.add_text("Source Meter 2: ")
                            dpg.add_text("Disconnected")
                        with dpg.group(horizontal=True):
                            dpg.add_button(label="Connect")
                            dpg.add_text("Arduino: ")
                            dpg.add_text("Disconnected")

                with dpg.group():
                    
                    voltages = np.linspace(-1.5, 1.5, int(abs((1.5 - -1.5) / 0.01)))
                    currents = np.sin(3 * voltages)

                    with dpg.plot(height=400, width=400):
                        
                        dpg.add_plot_axis(dpg.mvXAxis, label="x")
                        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
                        dpg.add_line_series(voltages, currents, parent="y_axis", tag="series_tag")
                        currents[10] = 100
                        dpg.set_value('series_tag', [voltages, currents])

        with dpg.tab(label="Broccoli"):
            dpg.add_text("This is the broccoli tab!")

        with dpg.tab(label="Cucumber"):
            dpg.add_text("This is the cucumber tab!")

dpg.set_primary_window("main_window", True)
dpg.create_viewport(title="IV Getter", width=650, height=700)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
