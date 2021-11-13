exports.up = function(knex) {
    return knex.schema.createTable('movies', table => {
        table.increments('id').primary().notNullable();
        table.string('title');
    }).createTable('users', table => {
        table.increments('id').primary().notNullable();
        table.string('gender')
        table.integer('age');
        table.integer('occupation');
        table.string('zip_code');
    }).createTable('ratings', table => {
        table.increments('id').primary().notNullable();
        table.integer('users_id').references('users.id');
        table.integer('movies_id').references('movies.id');
        table.integer('ratings');
        table.integer('timestamp');
    }).createTable('genres', table => {
        table.increments('id').primary().notNullable();
        table.integer('name');
    }).createTable('movies_genres', table => {
        table.increments('id').primary().notNullable();
        table.integer('movies_id').references('movies.id');
        table.integer('genres_id').references('genres.id');
    });
};

exports.down = function(knex) {
    return knex.schema.dropTable('ratings', true).dropTable('users', true).dropTable('movies', true).dropTable('genres', true).dropTable('movies_genres', true);
};