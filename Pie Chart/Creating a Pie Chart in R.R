library('ggplot2')

df_fuel_types <- read.csv('C:/Users/sbyeg/Downloads/pie_chart_data.csv', header = TRUE, sep = ',')

df_fuel_types

pie_chart <- ggplot(df_fuel_types, 
                    aes(x = "",
                        y = Number.of.Cars, 
                        fill = Engine.Fuel.Type)) +
                    geom_bar(stat = "identity",
                             width = 1) + 
                    coord_polar("y")
pie_chart

percentages <- paste0(round(df_fuel_types$Number.of.Cars/sum(df_fuel_types$Number.of.Cars) *100, 1), "%")

pie_chart <- pie_chart + geom_text(aes(label = percentages),
                                   position = position_stack(vjust = 0.5))
