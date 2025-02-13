BEGIN
    DISPLAY "Enter your budget for the month:"
    INPUT budget


    SET total_expenses = 0


    REPEAT
        DISPLAY "Enter an expense amount (or enter -1 to finish):"
        INPUT expense


        IF expense != -1 THEN
            total_expenses = total_expenses + expense
        ENDIF
    UNTIL expense == -1


    SET remaining_budget = budget - total_expenses


    DISPLAY "Total expenses: ", total_expenses
    DISPLAY "Remaining budget: ", remaining_budget


    IF remaining_budget > 0 THEN
        DISPLAY "You are under budget by ", remaining_budget
    ELSEIF remaining_budget < 0 THEN
        DISPLAY "You are over budget by ", ABS(remaining_budget)
    ELSE
        DISPLAY "You have exactly met your budget."
    ENDIF
END