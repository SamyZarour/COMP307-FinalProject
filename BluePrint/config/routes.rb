Rails.application.routes.draw do
	resources :users
	resources :courses do
		resources :comments
	end

	# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
	root 'pages#home'
	get 'profile' => 'pages#profile'

	get '/login' => 'sessions#new'
	post '/login' => 'sessions#create'
	get '/logout' => 'sessions#destroy'

	get '/signup' => 'users#new'
	post '/users' => 'users#create'
end
