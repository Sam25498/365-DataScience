library(ggplot2)

df_kdnuggets <- read.csv("C:/Users/sbyeg/Downloads/bar_line_chart_data.csv",
                         header = TRUE,
                         sep = ",")

combo <- ggplot(df_kdnuggets,
                aes(x = Year,
                    y = Participants, Python.Users)) +
        geom_bar(aes(y = Participants),
                 stat = "identity",
                 fill = "black") +
        geom_line(aes(y = Python.Users*max(Participants)),
                  stat = "identity",
                  color = "red",
                  size = 2) +
        scale_y_continuous(sec.axis = sec_axis(~./max(df_kdnuggets$Participants)*100,
                                               name = "Python Users in %")) +
        ggtitle("KD Nuggets Survey Python Users (2012 - 2019)")
combo                  
