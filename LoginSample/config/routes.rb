Rails.application.routes.draw do
	resources :courses do
		resources :comments
	end

	# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
	get '/login' => 'sessions#new'
	post '/login' => 'sessions#create'
	get '/logout' => 'sessions#destroy'

	get '/signup' => 'users#new'
	post '/users' => 'users#create'
end
