import { createApp } from 'vue'
import App from './App.vue'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faFilm, faStar, faTrash, faEdit } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faFilm, faStar, faEdit, faTrash);

createApp(App)
    .component("font-awesome-icon", FontAwesomeIcon)
    .mount('#app')
