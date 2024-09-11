function transform(input, emitter, context) {
 
    var part = input.A;
    var produce = input.B;
    var procure = input.C;
    var planner = input.D;
    var buyer = input.E;
    var nettable = input.F;
 
    var weeks = [
        { date: context.getHeader('G'), quantity: input.G },  
        { date: context.getHeader('H'), quantity: input.H },   
        { date: context.getHeader('I'), quantity: input.I },   
        { date: context.getHeader('J'), quantity: input.J }    
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
