import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.add_text("Hello")

dpg.destroy_context()