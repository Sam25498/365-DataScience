library("ggplot2")

df_used_cars <- read.csv("C:/Users/sbyeg/Downloads/bar_chart_data.csv", 
                         header = TRUE,
                         sep = ",")

bar_chart <- ggplot(df_used_cars, 
                    aes(x = Cars.Listings, 
                        y = Brand)) +
  geom_bar(stat = "identity", 
           width = 0.8,
           color = "navy", 
           fill = "navy") +
  ggtitle("Cars Listings by Brand") + 
  theme_classic() + theme(axis.text.x = element_text(angle = 45,
                                                     hjust = 1))  +
  labs(x = NULL,
       y = "Number of Listings")


bar_chart
