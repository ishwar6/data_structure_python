function transform(input, emitter, context) {
     
    var part = input.A;
    var produce = input.B;
    var procure = input.C;
    var planner = input.D;
    var buyer = input.E;
    var nettable = input.F;
    
    
    var rowWithDates = context.getArguments()['dateRow'];  
    
    
    var weeks = [
        { date: rowWithDates.G, quantity: input.G },  
        { date: rowWithDates.H, quantity: input.H },  
        { date: rowWithDates.I, quantity: input.I }, 
        { date: rowWithDates.J, quantity: input.J }   
    ];
 
    weeks.forEach(function(week) {
        if (week.quantity && week.quantity !== '') {   
            emitter.emit({
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
