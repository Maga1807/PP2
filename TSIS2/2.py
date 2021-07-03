def interpret(command)
    output = ""

   command.split('').each_with_index { |character, idx|

        if character == "G"
            output += "G"
        elsif character == "("
            if command[idx + 1] == ")"
                output += "o"
            elsif command[idx + 1] == "a" && command[idx + 2] = "l" && command[idx + 3] = ")"
                output += "al"
            end
        end
 }
    return output
end
