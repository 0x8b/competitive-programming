w, h, alpha = gets.split.map &:to_f

h, w = [w, h].sort

if alpha > 90
  alpha = 180 - alpha
end

if alpha == 0
  puts w * h
elsif alpha == 90
  puts h * h
else
  alpha = (alpha / 180) * Math::PI

  if (alpha / 2) >= Math.atan2(h, w)
    # area of diamond
    puts h * (h / Math.sin(alpha))
  else
    x = Math.tan(alpha / 2) * (h / 2)
    y = Math.tan(alpha / 2) * (w / 2)
    a = (w / 2) - x
    b = (h / 2) - y
    c = Math.tan(alpha) * a
    d = Math.tan(alpha) * b

    rectangle_area = w * h
    bigger_triangle_area = (a * c) / 2
    smaller_triangle_area = (b * d) / 2

    shadowed_area = rectangle_area - 2 * bigger_triangle_area - 2 * smaller_triangle_area

    puts shadowed_area
  end
end