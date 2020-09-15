const mongoose = require('mongoose')
const UserSchema  = new mongoose.Schema({   
    Title: {
        type: String,
    },
    Sub_Title: {
        type: String
    },
    Peoples: {
        type: String,
        Id: {
            type: String, 
            Nome: String,
            Cargo: String,
            Imagem: String,
            Twitter: String,
            Facebook: String,
            Gmail: String,
            linkedin: String,
            unique: true

        }
    }             
}
)