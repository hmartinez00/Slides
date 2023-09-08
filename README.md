# RELATIONSHIPS

## ONE TO ONE
### Pasos preliminares
1. Nos apoyamos en el modelo user, y creamos otro modelo llamado phone.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Phone.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_09_190213_create_phones_table.php"

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
    $table->unsignedBigInteger('user_id');

"nombredelmodelo_id" (minusculas)

4. Migramos.

> Nota: El modelo que contiene a la clave foranea "pertenece a (BelongsTo)" el modelo que no la contiene.


### Vinculaciones
5. Vinculamos User con Phone

En "Slides\laravel\relationships\app\Models\User.php" creamos una funcion publica:

    public function phone(): HasOne
    {
        return $this->hasOne(Phone::class);
    }

Esto es para que cuando solicitemos $user->phone se nos devuelva todos los phone que tiene el usuario. Solo tiene uno, de manera que solo se devolvera uno (HasOne). Como usamos la convencion de nombres "user_id" en la clave foranea, ya laravel sabe que que debe acudir al campo "id" del modelo que estamos relacionando con "Phone".

Si la "foreing_key" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function phone(): HasOne
    {
        return $this->hasOne(Phone::class, "foreing_key", "field");
    }

6. Vinculamos Phone con User

En "Slides\laravel\relationships\app\Models\Phone.php" creamos una funcion publica:

    public function user():BelongsTo
    {
        return $this->belongsTo(User::class);
    }

Si la "foreing_key" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function user():BelongsTo
    {
        return $this->BelongsTo(User::class, "foreing_key", "field");
    }


> Hasta este punto culmina el proceso de vinculacion. El proximo paso es la creacion de la estructura de VIEWS o la APIS.


### Poblando la Base de datos
7. Creamos los Seeder para el User y el Phone.

8. En el "Slides\laravel\relationships\database\seeders\DatabaseSeeder.php" incorporamos el "call" a los seeder:

        $this->call([
            UserSeeder::class,
            PhoneSeeder::class,
        ]);

9. En el "Slides\laravel\relationships\database\seeders\UserSeeder.php" actualizamos:

        User::create([
            'id' => 1,
            'name' => 'example',
            'email' => 'example@example.com',
            'password' => Hash::make('12345678'),
        ]);

y en el "Slides\laravel\relationships\database\seeders\PhoneSeeder.php" actualizamos:

        Phone::create([
            'prefix' => +58,
            'phone_number' => 11111111,
            'user_id' => 1,
        ]);

10. Montamos la info con "php artisan bd:seed".

### Gestionando la VIEW

> Usaremos el modelo primario, el modelo donde NO esta la foreing_key.

11. Creamos el controlador de la vista "UserController".

12. En el "Slides\laravel\relationships\routes\web.php" creamos la ruta usando el controlador:

Route::get('/', [UserController::class, 'index'])->name('index');

13. En el "Slides\laravel\relationships\app\Http\Controllers\UserController.php" creamos la funcion:

    public function index()
    {
        $user = User::find(1);
        return view('index', compact('user'));
    }

14. Creamos finalmente la vista:

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>index</title>
    </head>
    <body>
        <h1>{{ $user->email }}</h1>
        <h1>{{ $user->phone->prefix }}</h1>
        <h1>{{ $user->phone->phone_number }}</h1>
    </body>
    </html>
```

### Gestionando la API
15. Creamos el Resource con:
    php artisan make:resource UserResource

16. En "Slides\laravel\relationships\app\Http\Resources\UserResource.php" modificamos el return:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phone' => '('.$this->phone->prefix.')'.$this->phone->phone_number,
        ];

17. En "Slides\laravel\relationships\routes\api.php" modificamos el Route:

Route::get('/user', function (Request $request) {
    $user = User::find(1);
    return new UserResource($user);
});

> Hasta este punto hemos gestionado la entrega de los datos en vista y en API (min 40:16).


## ONE TO MANY
> Para este tipo de relacion tendremos que modificar la relacion entre los modelos.

### Vinculaciones
1. En el modelo prioritario "Slides\laravel\relationships\app\Models\User.php" hacemos el cambio de "HasOne" a "HasMany".

    public function phones(): HasMany
    {
        return $this->hasMany(Phone::class);
    }

Con esto ya se ha construido la relacion ONE TO MANY.

### Repoblando la Base de datos
2. Añadimos otro dato con nuestros PhoneSeeder y comentamos el UserSeeder en el DatabaseSeeder para que no se ejecute y aplicamos "php artisan db:seed".

### Gestionando la VIEW
3. Actualizamos la vista:

```html
    <h1>{{ $user->name }} Phones:</h1>
    <ul>
    @foreach ($user->phones as $phone)
        <li>{{ $phone->prefix }} {{ $phone->phone_number }}</li>
    @endforeach
    </ul>  
```

### Gestionando la API
4. En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" Actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
        ];

> Aca hemos culminado el proceso para crear una relacion ONE TO MANY (min 47:21).

## MANYTOMANY
### Pasos preliminares
1. Creamos un nuevo modelo llamado "Role".

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Role.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_28_201223_create_roles_table.php"

4. Migramos.

### Creando tabla de Paso para vinculaciones
> Aca se emplea no una llave foranea sino una tabla de paso entro dos modelos para lograr las vinculaciones. La convencion de nomenclatura es la siguiente: modelo1_modelo2 (ordenados alfabeticamente).

5. Ceamos el archivo de migracion (No lleva modelo asociado!!) con php artisan make:migration create_role_user_table

6. (min 52:41) En "Slides\laravel\relationships\database\migrations\2023_08_28_203333_create_role_user_table.php" modificar el Schema para agregar las "foreing_key" como sigue:

        Schema::create('role_user', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('role_id');
            $table->unsignedBigInteger('user_id');
            $table->timestamps();
        });

Podriamos añadir algo de informacion extra.

        Schema::create('role_user', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('role_id');
            $table->unsignedBigInteger('user_id');
            $table->string('added_by')->nullable();
            $table->timestamps();
        });

7. Vovio a Migrar.

### Vinculaciones
8. Vinculamos User con Role

En "Slides\laravel\relationships\app\Models\User.php"

    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class);
    }

o

    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class)->withPivot('added_by');
    }

Si la "tabla_de paso" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class, 'role_user', 'user_id', 'role_id');
    }

9. vinculamos Role con User

En "Slides\laravel\relationships\app\Models\Role.php" creamos la funcion publica:

    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class);
    }
    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class)->withPivot('added_by');
    }

Si la "tabla_de paso" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class, 'role_user', 'user_id', 'role_id');
    }

### Repoblando la Base de datos
10. Creamos el Seeder pare el modelo Role.

11. En el "Slides\laravel\relationships\database\seeders\DatabaseSeeder.php" incorporamos el "call" a los seeder:

        $this->call([
            UserSeeder::class,
            PhoneSeeder::class,
            RoleSeeder::class,
        ]);

12. En el "Slides\laravel\relationships\database\seeders\UserSeeder.php"

        User::create([
            'id' => 1,
            'name' => 'example',
            'email' => 'example@example.com',
            'password' => Hash::make('12345678'),
        ]);
        User::create([
            'id' => 2,
            'name' => 'example2',
            'email' => 'example2@example2.com',
            'password' => Hash::make('12345678'),
        ]);
        User::create([
            'id' => 3,
            'name' => 'example3',
            'email' => 'example3@example3.com',
            'password' => Hash::make('12345678'),
        ]);

y en el "Slides\laravel\relationships\database\seeders\RoleSeeder.php" actualizamos:

        Role::create([
            'id' => 1,
            'name' => 'admin'
        ]);
        Role::create([
            'id' => 2,
            'name' => 'staff'
        ]);
        Role::create([
            'id' => 3,
            'name' => 'user'
        ]);
        Role::create([
            'id' => 4,
            'name' => 'guest'
        ]);

        // Aca vamos a hacer la asociacion!
        DB::table('role_user')->insert([
            'role_id' => 1,
            'user_id' => 1,
            'added_by' => 'hmartinez',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 2,
            'user_id' => 1,
            'added_by' => 'luis',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 1,
            'user_id' => 2,
            'added_by' => 'jose',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 3,
            'user_id' => 2,
            'added_by' => 'hmartinez',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 4,
            'user_id' => 3,
            'added_by' => 'maria',
        ]);

13. Montamos la info con "php artisan bd:seed" (Aca hicimos un "refresh" previo para evitar montar info duplicada!).

### Gestionando la VIEW
14. Actualizamos la vista: 

```html
    <h1>{{ $user->name }} Roles:</h1>
    <ul>
    @foreach ($user->roles as $role)
        <li>{{ $role->name }} Added By: {{ $role->pivot->added_by}}</li>
    @endforeach
    </ul>  
```

### Gestionando la API
15. En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" Actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
            'roles' => $this->roles
        ];

> Aca culmina el proceso de MANY TO MANY (min 01:10:43)


## HAS ONE THROUGH
> Esta es el tipo de relacion que tiene un modelo con otro indirectamente, apoyandose en la relacion que tienen ambos, con un tercero.

### Pasos preliminares
1. Creamos otro modelo llamado phone.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Sim.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_29_145616_create_sims_table.php"

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
    $table->unsignedBigInteger('phone_id');

### Vinculaciones

4. Vinculamos Phone con Sim

En "Slides\laravel\relationships\app\Models\Phone.php" creamos una funcion publica:

    public function sim():HasOne
    {
        return $this->hasOne(Sim::class);
    }

5. Vinculamos Sim con Phone

En "Slides\laravel\relationships\app\Models\Sim.php" creamos una funcion publica:

    public function phone():BelongsTo
    {
        return $this->belongsTo(Phone::class);
    }

6. Vinculamos User con Sim "a traves" de Phone el cual ya esta relacionado con Sim.

En el "Slides\laravel\relationships\app\Models\User.php" creamos una funcion publica:

    public function phoneSim():HasOneThrough
    {
        return $this->hasOneThrough(Sim::class, Phone::class);
    }

Si no respetara la convencion de laravel, habria que especificar tres parametros en la funcion:

    public function phoneSim():HasOneThrough
    {
        return $this->hasOneThrough(Sim::class, Phone::class, [sim_param], [phone_param], [local_key]);
    }

### Repoblando la Base de datos
.

### Gestionando la VIEW
. Actualizamos la vista:

```html
    <h1>{{ $user->name }} Roles:</h1>
    <h3>{{ $user->phoneSim }}</h3>
    <ul>
    @foreach ($user->roles as $role)
        <li>{{ $role->name }} Added By: {{ $role->pivot->added_by}}</li>
    @endforeach
    </ul> 
```

### Gestionando la API
. 

> (min 01:19:17)


## HAS ONE THROUGH
> Para este tipo de relacion tendremos que modificar la relacion entre los modelos.

### Vinculaciones
1. En el "Slides\laravel\relationships\app\Models\Phone.php" hacemos el cambio de "HasOne" a "HasMany".

    public function sims():HasMany
    {
        return $this->hasMany(Sim::class);
    }

2. En el "Slides\laravel\relationships\app\Models\User.php" hacemos el cambio de "HasOneThrough" a "HasManyThrough".

    public function phoneSims():HasManyThrough
    {
        return $this->hasManyThrough(Sim::class, Phone::class);
    }

> (min 01:22:29)

## MORPHONE
### Pasos preliminares
1. Creamos otro modelo llamado post e image.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Post.php" y en "Slides\laravel\relationships\app\Models\Image.php":
    protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_30_165644_create_posts_table.php" y "Slides\laravel\relationships\database\migrations\2023_08_30_170049_create_images_table.php".

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
            $table->unsignedBigInteger('imageable_id');
            $table->string('imageable_type');


"nombredelmodelo(able)_id" (minusculas)

### Vinculaciones
4. "Morfeamos" Image

En "Slides\laravel\relationships\app\Models\Image.php" creamos la funcion publica:

    public function imageable():MorphTo
    {
        return $this->morphTo();
    }

5. "Morfeamos" Post

En "Slides\laravel\relationships\app\Models\Post.php" creamos la funcion publica:

    public function image():MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }

6. "Morfeamos" User

En el "Slides\laravel\relationships\app\Models\User.php"

    public function image():MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }


### Repoblando la Base de datos
.

### Gestionando la VIEW
. Actualizamos la vista:

```html
    <h1>{{ $user->image->url }}</h1>
```

### Gestionando la API
. Actualizamos la API

En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
            'roles' => $this->roles,
            'image' => $this->image,
        ];

> (01:36:36)

## MORPHMANY
### Vinculaciones
1. En "Slides\laravel\relationships\app\Models\Post.php" hacemos el cambio de "MorphOne" a "MorphMany":

    public function image():MorphMany
    {
        return $this->morphMany(Image::class, 'imageable');
    }

y en "Slides\laravel\relationships\app\Models\User.php" hacemos el cambio de "MorphOne" a "MorphMany":

    public function image():MorphMany
    {
        return $this->morphMany(Image::class, 'imageable');
    }

### Repoblando la Base de datos
### Gestionando la VIEW
### Gestionando la API

> (min 01:40:15)

## MORPHTOMANY
### Pasos preliminares
1. Creamos los nuevos modelos llamados "Video" y "Tag".

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Video.php" y "Slides\laravel\relationships\app\Models\Tag.php"
    protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_09_04_141434_create_videos_table.php" y "Slides\laravel\relationships\database\migrations\2023_09_04_141832_create_tags_table.php".

### Creando tabla de Paso para vinculaciones
> Aca se emplea no una llave foranea sino una tabla de paso entro dos modelos para lograr las vinculaciones. Aca hay que tener cuidado, esta convencion de nombre no fue aclarada en el video, es nueva y no se parece a nada de lo tratado anteriormente.

4. Ceamos el archivo de migracion (No lleva modelo asociado!!) con php artisan make:migration create_taggables_table

5. En "Slides\laravel\relationships\database\migrations\2023_09_04_142747_create_taggables_table.php" modificar el Schema:

        Schema::create('taggables', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('tag_id');
            $table->unsignedBigInteger('taggable_id');
            $table->unsignedBigInteger('taggable_type');
            $table->timestamps();
        });

6. Migramos.

### Vinculaciones
7. Morfeamos "Post" y "Video"

En "Slides\laravel\relationships\app\Models\Post.php"

    public function tags():MorphToMany
    {
        return $this->morphToMany(Tag::class, 'taggable');
    }

y en "Slides\laravel\relationships\app\Models\Video.php"

    public function tags():MorphToMany
    {
        return $this->morphToMany(Tag::class, 'taggable');
    }

finalmente en "Slides\laravel\relationships\app\Models\Tag.php"

    public function posts():MorphToMany
    {
        return $this->morphedByMany(Post::class, 'taggable');
    }
    public function videos():MorphToMany
    {
        return $this->morphedByMany(Video::class, 'taggable');    
    }

> Aca culmina el proceso de MorphToMany

### Repoblando la Base de datos
### Gestionando la VIEW
### Gestionando la API


> Hasta aca el contenido de relaciones entre modelos en Laravel.


# MIDDLEWARE Y API AUTH

## Aplicando directamente a rutas.
1. Creamos nuestro primer middleware con: php artisan make:middleware Example

2. En "Slides\laravel\middlewareauth\app\Http\Kernel.php" agregamos a la lista "protected $middlewareAliases" el elemento:

    'example' => \App\Http\Middleware\Example::class,

3. Creamos el controlador del middleware. Sera el siguiente: "Slides\laravel\middlewareauth\app\Http\Controllers\ExampleController.php"

4. Actualizamos el controlador:

    public function index()
    {
        return response()->json('Hellow World!', 200); #Recuerda que esto protege una ruta api!
    }

5. En "Slides\laravel\middlewareauth\routes\api.php" agregamos:

Route::middleware('example')->get('/', [ExampleController::class, 'index']);

El middleware de proteccion se llama "middleware('example')" debido a que asi fue registrado en "Kernel.php" (Paso: 2).

Adicionalmente agregaremos una ruta no protegida para comparar:

Route::get('/no-access', [ExampleController::class, 'noAccess'])->name('no-access');

6. Agregamos al controlador otra funcion publica:

    public function noAccess()
    {
        return response()->json('No access', 200);
    }

7. En "Slides\laravel\middlewareauth\app\Http\Middleware\Example.php" actualizamos:

    public function handle(Request $request, Closure $next): Response
    {
        return redirect()->route('no-access');
        // return $next($request);
    }

8. Migramos.

9. Levantamos el servicio y podemos acceder a la ruta: http://127.0.0.1:8000/api/, pero con la estructura actual, seremos redireccionados inmediatamente a: http://127.0.0.1:8000/api/no-access

Recibiendo la respuesta predeterminada en el paso 6 'No access'.

Si cambiamos en  "Slides\laravel\middlewareauth\app\Http\Middleware\Example.php" actualizamos:

    public function handle(Request $request, Closure $next): Response
    {
        // return redirect()->route('no-access');
        return $next($request);
    }

Alli podremos acceder directamente a la ruta: http://127.0.0.1:8000/api/

Recibiendo la respuesta predeterminada en el paso 4 'Hellow World!'


## Aplicando a grupos de rutas.
1. Podemos usar la funcion group(). En "Slides\laravel\middlewareauth\routes\api.php" reintroducimos la primera ruta quitando el middleware. queda asi:

Route::middleware('example')->group(function () {
    Route::get('/', [ExampleController::class, 'index']);
});

2. Si se aplican varios middleware a dicho grupo de rutas se usa un array, y en caso de excluir la accion de un middleware sobre una ruta concreta del grupo se usa el metodo "->withoutMiddleware('...')". En abstracto seria como sigue:

Route::middleware(['middleware-1', 'middleware-2'..., 'middleware-N'])->group(function () {
    Route::get('/ruta-1', [Controller::class, 'function']);
    Route::get('/ruta-2', [Controller::class, 'function']);
    Route::get('/ruta-3', [Controller::class, 'function'])->withoutMiddleware('middleware-2');
    Route::get('/ruta-4', [Controller::class, 'function']);
    ...
    Route::get('/ruta-M', [Controller::class, 'function']);
});


## Usando el método contructor en el Controller.
1. Agregamos al principio del archivo controlador:

...
    class ExampleController extends Controller
    {
        public function __construct()
        {
            $this->middleware('example');
        }
        ...
    }

> Esto puede generar peticion circular y tumba la pagina!


## Desarrollando un sistema de autenticacion.
> Nos apoyaremos en el modelo User que viene por defecto!!

1. Crearemos un controlador basico llamado AuthController.

2. Creamos la CustomRequest para la creacion de usuarios con: php artisan make:request CreateUserRequest.

3. Creamos la CustomRequest para la autenticacion de usuarios con: php artisan make:request LoginUserRequest.

4. En "Slides\laravel\middlewareauth\app\Http\Requests\CreateUserRequest.php" actualizamos:

    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            'name' => 'required',
            'email' => 'required|email|unique:users,email',
            'password' => 'required',
        ];
    }

5. En "Slides\laravel\middlewareauth\app\Http\Requests\LoginUserRequest.php" actualizamos:

    public function authorize(): bool
    {
        return true;
    }

    public function rules(): array
    {
        return [
            'email' => 'required|email',
            'password' => 'required',
        ];
    }

6. En "Slides\laravel\middlewareauth\app\Http\Controllers\AuthController.php" agregamos las funciones: 

    public function createUser(CreateUserRequest $request)
    {
        $user = User::create([
            'name' => $request->name,
            'email' => $request->email,
            'password' => Hash::make($request->password),
        ]);

        return response()->json([
            'status' => true,
            'message' => 'User created succesfully',
            'token' => $user->createToken('API TOKEN')->plainTextToken
        ], 200);
    }

    public function loginUser(LoginUserRequest $request)
    {
        if(!Auth::attempt($request->only(['email', 'password'])))
        {
            return response()->json([
                'status' => false,
                'message' => 'Email & Password do not match with our records',
            ], 401);
        }

        $user = User::where('email', $request->email)->first();

        return response()->json([
            'status' => true,
            'message' => 'User logged in successfully',
            'token' => $user->createToken("API TOKEN")->plainTextToken
        ], 200);
    }

7. En "Slides\laravel\middlewareauth\routes\api.php" creamos nuestras rutas:

    Route::post('/create', [AuthController::class, 'createUser']);
    Route::post('/login', [AuthController::class, 'loginUser']);

8. Podemos enviar la peticion a la API

POST http://127.0.0.1:8000/api/create

Body:
{
  "name": "hmartinez",
  "email": "hmartinez@email.com",
  "password": "XXXXXX"
}

Luego de esta configuracion damos Send.

Ahora para entrar a a la ruta api/user:

GET http://127.0.0.1:8000/api/user

Headers:
Accept          : application/json
User-Agent      : Thunder Client (https://www.thunderclient.com)
Authorization   : Bearer 1|Rb4KBKVcQyg9kO54tOhLKZprFFEUpQrMLxJ3CHn47d31376a
Content-Type    : application/json

Luego de esta configuracion damos Send.


# AUTH, BREEZE JETSTREAM

## BREEZE
1. Descargar Breeze con: 
composer require laravel/breeze --dev

2. Instalar scafolding con:
php artisan breeze:install

> Solicitara configuracion. Introducir:
> stack: blade
> dark mode support: yes
> testing framework: [Enter]
>
> Aca iniciara la instalacion.

Se actualizaran los directorios y archivos:
* "\resources\views"
* "\routes\web.php"
* "\app\Http\Controllers\Auth"
* "\app\Http\Controllers\ProfileController.php".

3. Antes de apreciar los resultados de la estructura creada, Migramos.

4. Ejecutar: npm install

5. Ejecutar: npm run dev 
Dejar activo el terminal!

6. Ahora si, para poder ver los resultados, levantar el servidor local.


> Hagamos un ejemplo de adicion de ruta:

7. Creamos ExampleController.

8. En "Slides\laravel\authbreeze\routes\web.php" agregamos:

Route::middleware('auth')->group(function () {
    ...
    Route::get('/example', [ExampleController::class, 'index'])->name('example');
});

9. En "Slides\laravel\authbreeze\app\Http\Controllers\ExampleController.php" actualizamos:

    public function index()
    {
        $user = Auth::user();
        return view('example', compact('user'));
    }

10. Podemos crear una nueva vista en 
"Slides\laravel\authbreeze\resources\views\example.blade.php" con el siguiente contenido

```html
<x-app-layout>
    <x-slot name="header">
        <h2 class="font-semibold text-xl text-gray-800 dark:text-gray-200 leading-tight">
            Example Page
        </h2>
    </x-slot>

    <div class="py-12">
        <div class="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div class="bg-white dark:bg-gray-800 overflow-hidden shadow-sm sm:rounded-lg">
                <div class="p-6 text-gray-900 dark:text-gray-100">
                    <p>Hellow {{ $user->name }}</p>
                </div>
            </div>
        </div>
    </div>
</x-app-layout>
```

> Hasta aca lo correspondiente a Breeze (min 00:47:14)

## JETSTREAM

