important that we keep the dims, when we mandate that we find the min per row(1) or column(0). 

again a zero error is important. where we replace the 0 division with a one. this is not a universal implemenetation (i think). it works in this case as 

data_range is always positive and its range will be tiny, making the denomiator X- min also &lt; eps. 

still feels a bit wierd