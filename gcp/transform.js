function transform(input, emitter, context) {
    
    var part = input.A;
    var produce = input.B;
    var procure = input.C;
    var planner = input.D;
    var buyer = input.E;
    var nettable = input.F;
    
     
    var weeks = [
        { date: "WK01", quantity: input.G },  
        { date: "WK02", quantity: input.H },  
        { date: "WK03", quantity: input.I },  
        { date: "WK04", quantity: input.J }   
    ];

    
    if (nettable === "Confirmed Purchase Orders") {
        weeks.forEach(function (week) {
            // Emit a new record for each date (week)
            emitter.emit({
                A: part,
                B: produce,
                C: procure,
                D: planner,
                E: buyer,
                F: "Confirmed Purchase Orders",   
                G: week.date,                   
                H: week.quantity                
            });
        });
    } else if (nettable === "Demand") {
        weeks.forEach(function (week) {
           
            emitter.emit({
                A: part,
                B: produce,
                C: procure,
                D: planner,
                E: buyer,
                F: "Demand",                     
                G: week.date,                  
                H: week.quantity                 
            });
        });
    }
}
