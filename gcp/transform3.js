function transform(input, emitter, context) {
 
    var part = input.A;
    var produce = input.B;
    var procure = input.C;
    var planner = input.D;
    var buyer = input.E;
    var nettable = input.F;
    
    
    var weekColumns = [
        { date: input.G, quantity: input.G },  
        { date: input.H, quantity: input.H },  
        { date: input.I, quantity: input.I },  
        { date: input.J, quantity: input.J }   
    ];
     
    weekColumns.forEach(function(week) {
        if (week.quantity && week.quantity !== '') {   
            emitter.emit({
                file: input.file,           
                sheet: input.sheet,         
                A: part,                     
                B: produce,                
                C: procure,                  
                D: planner,                
                E: buyer,                    
                F: nettable,                
                G: week.date,               
                H: week.quantity           
            });
        }
    });
}
